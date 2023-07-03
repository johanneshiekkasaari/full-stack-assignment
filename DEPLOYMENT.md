# Deployment plan and improvment ideas

- [x] odin-ui: Rewrite
- [x] odin-api: Rewrite
- [ ] odin-ui: Write a dockerfile
- [ ] odin-api: Write a dockerfile
- [ ] terraform: Set up ECRs in AWS for both admin-ui and admin-api
- [ ] odin-ui: Utilize github actions to build and push docker image to ECR
- [ ] odin-api: Utilize github actions to build and push docker image to ECR
- [ ] terraform: set up a kubernetes cluster with an load balancer and set up Route53 zones for DNS
- [ ] helm-chart: Write helm chart with deployment and service definitions for both ui and api
- [ ] helm-chart: write an ingress definition so both api and ui can be accessed from outside k8s
- [ ] odin-ui: allow defining odin api url via environment variables and write helm chart so that it can be manipulated via helm chart values

# Improvement ideas

- [ ] odin-api: rewrite the terrible `odin-api/osm.py` to use a more modern library
- [ ] odin-api: cache the results of the query in `odin-api/osm.py`, right now it queries them every time
- [ ] odin-api: Define all endpoint response values using pydantic so the documentation works and python types would work
- [ ] odin-api: rewrite odin-api/image.py so that it gets the image metadata from a db like auroraDB and the images are stored in S3
- [ ] odin-api: clean up requirements.txt
- [ ] odin-ui: spend time actually thinking about making the UI pretty instead of MVP
