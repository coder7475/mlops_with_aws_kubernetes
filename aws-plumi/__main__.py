"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

# Create a VPC
vpc = aws.ec2.Vpc("my-vpc", 
                  cidr_block="10.0.0.0/16",
                  tags={
                      "Name": "my-vpc"
                  })

pulumi.export("vpc_id", vpc.id)

# Crete the Public Subnet
public_subnet = aws.ec2.Subnet("public-subnet",
                               vpc_id=vpc.id,
                               cidr_block="10.0.1.0/24",
                               availability_zone="ap-southeast-1a",
                               map_public_ip_on_launch=True,
                               tags={
                                   "Name": "my-public-subnet"
                               })

pulumi.export("public_subnet_id", public_subnet.id)

# Create a private subnet
private_subnet = aws.ec2.Subnet("private-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.2.0/24",
    availability_zone="ap-southeast-1a",
    tags={
        "Name": "my-private-subnet"
    }
)

pulumi.export("private_subnet_id", private_subnet.id)


# Create the Internet Gateway
igw = aws.ec2.InternetGateway("IGW", 
                               vpc_id=vpc.id,
                               tags={
                                "Name": "my-internet-gateway"
                               }
                            )

pulumi.export("igw_id", igw.id)


# Create a route table for the public subnet
public_route_table = aws.ec2.RouteTable("public-route-table", 
                                        vpc_id=vpc.id,
                                        tags={
                                            "Name": "my-public-route-table"
                                        }
)

# Create a route in the route table for IGW
route = aws.ec2.Route("igw-route", 
                      route_table_id=public_route_table.id,
                      destination_cidr_block="0.0.0.0/0",
                      gateway_id=igw.id
)

# Associate the route table with the public subnet
route_table_association = aws.ec2.RouteTableAssociation("public-route-table-association",
    subnet_id=public_subnet.id,
    route_table_id=public_route_table.id
)

pulumi.export("public_route_table_id", public_route_table.id)


# Create the NAT Gateway
eip = aws.ec2.Eip("nat-eip", vpc=True) # allocate elastic ip for the NAT gateway

nat_gateway = aws.ec2.NatGateway("nat-gateway", 
                                 subnet_id=public_subnet.id,
                                 allocation_id=eip.id,
                                 tags={
                                     "Name": "my-nat-gateway"
                                 }
)

pulumi.export("nat_gateway_id", nat_gateway.id)

# Create a route table for the private subnet
private_route_table = aws.ec2.RouteTable("private-route-table",
    vpc_id=vpc.id,
    tags={
        "Name": "my-private-route-table"
    }
)

# Create a route in the route table for the NAT Gateway
private_route = aws.ec2.Route("nat-route",
    route_table_id=private_route_table.id,
    destination_cidr_block="0.0.0.0/0",
    nat_gateway_id=nat_gateway.id
)

# Associate the route table with the private subnet
private_route_table_association = aws.ec2.RouteTableAssociation("private-route-table-association",
    subnet_id=private_subnet.id,
    route_table_id=private_route_table.id
)

pulumi.export("private_route_table_id", private_route_table.id)


