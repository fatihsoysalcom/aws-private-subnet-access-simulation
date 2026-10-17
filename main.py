import os

def simulate_private_subnet_access(has_nat_gateway: bool, has_vpc_endpoint_s3: bool):
    """
    Simulates network access from an instance in a private subnet based on
    the presence of a NAT Gateway and an S3 VPC Endpoint.
    """
    print(f"\n--- Simulating Access from Private Subnet ---")
    print(f"  Configuration: NAT Gateway {'ENABLED' if has_nat_gateway else 'DISABLED'}, S3 VPC Endpoint {'ENABLED' if has_vpc_endpoint_s3 else 'DISABLED'}")

    # Scenario 1: Accessing a general internet resource (e.g., downloading a public package)
    # This requires outbound internet access, which is provided by a NAT Gateway.
    print("\n  1. Attempting to access a general internet resource (e.g., public package repository)...")
    if has_nat_gateway:
        # NAT Gateway provides a path for instances in private subnets to connect to the internet.
        print("    ✅ Success: NAT Gateway routes outbound traffic to the internet.")
    else:
        # Without a NAT Gateway, private subnets cannot initiate connections to the internet.
        print("    ❌ Failure: No NAT Gateway. Outbound internet access is blocked for private subnet.")

    # Scenario 2: Accessing an AWS S3 service
    # This can be done privately via a VPC Endpoint or via the public internet endpoint if a NAT Gateway is present.
    print("\n  2. Attempting to access an AWS S3 service...")
    if has_vpc_endpoint_s3:
        # VPC Endpoints allow private access to specific AWS services (like S3)
        # without traversing the internet, keeping traffic within the AWS network.
        print("    ✅ Success: VPC Endpoint for S3 allows private access within the AWS network.")
    elif has_nat_gateway:
        # If no VPC Endpoint, S3 can still be accessed if a NAT Gateway is present,
        # but the traffic goes over the public internet to S3's public endpoint.
        print("    ✅ Success: No VPC Endpoint, but NAT Gateway allows access via S3's public endpoint (traffic leaves VPC to internet, then back to AWS).")
    else:
        # Without either, access to S3 is blocked from a private subnet.
        print("    ❌ Failure: No VPC Endpoint and no NAT Gateway. Access to S3 is blocked.")

    # Scenario 3: Accessing another AWS service (e.g., DynamoDB) without a specific VPC Endpoint for it
    # This typically relies on NAT Gateway for outbound access to the service's public endpoint.
    print("\n  3. Attempting to access AWS DynamoDB (assuming no specific VPC Endpoint for DynamoDB)...")
    if has_nat_gateway:
        # For AWS services without a configured VPC Endpoint, NAT Gateway enables access
        # by routing traffic to the service's public endpoint over the internet.
        print("    ✅ Success: NAT Gateway allows access to DynamoDB via its public endpoint.")
    else:
        # Without a NAT Gateway, access to DynamoDB's public endpoint is blocked.
        print("    ❌ Failure: No NAT Gateway. Access to DynamoDB is blocked.")

# --- Main simulation logic ---
print("--- AWS Private Subnet Network Access Simulation ---")
print("This simulation demonstrates the different access patterns for instances in a private subnet")
print("depending on the presence of a NAT Gateway and VPC Endpoints.")

# Case 1: No NAT Gateway, No VPC Endpoints
# Instances in private subnets are isolated.
simulate_private_subnet_access(has_nat_gateway=False, has_vpc_endpoint_s3=False)

# Case 2: Only NAT Gateway
# Instances can reach the internet and AWS services via their public endpoints.
simulate_private_subnet_access(has_nat_gateway=True, has_vpc_endpoint_s3=False)

# Case 3: Only S3 VPC Endpoint
# Instances can privately reach S3, but cannot reach the general internet or other AWS services (without their own endpoints).
simulate_private_subnet_access(has_nat_gateway=False, has_vpc_endpoint_s3=True)

# Case 4: Both NAT Gateway and S3 VPC Endpoint
# Instances can reach the internet (via NAT) and privately reach S3 (via endpoint).
# For S3, the VPC Endpoint path is preferred for security and cost.
simulate_private_subnet_access(has_nat_gateway=True, has_vpc_endpoint_s3=True)

print("\n--- Simulation Complete ---")
print("Key takeaway: NAT Gateway for general internet access, VPC Endpoints for private AWS service access.")
print("When both are present, VPC Endpoints are generally preferred for AWS service access for security and cost reasons.")
