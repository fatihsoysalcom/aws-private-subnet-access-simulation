# AWS Private Subnet Access Simulation

This example simulates network access patterns from an instance located in an AWS private subnet. It demonstrates how the presence of a NAT Gateway enables outbound internet access and how a VPC Endpoint allows private, secure access to specific AWS services like S3, without traversing the public internet. The simulation highlights the different outcomes for accessing general internet resources versus AWS services under various network configurations.

## Language

`python`

## How to Run

Save the code as `main.py`. Open a terminal in the same directory and run:
`python main.py`

## Original Article

This example accompanies the Turkish article: [NAT Gateway mi, VPC Endpoints mi: Bulut Ağınız İçin Doğru Seçim](https://fatihsoysal.com/blog/nat-gateway-mi-vpc-endpoints-mi-bulut-aginiz-icin-dogru-secim/).

## License

MIT — see [LICENSE](LICENSE).
