# RyuGoo-Saba
RyuGoo-Saba is an execution engine aimed at running [Common Workflow Language (CWL)](https://www.commonwl.org) on cloud computing. The differences from the other cloud enabled CWL runners like [Toil](https://github.com/BD2KGenomics/toil) and [Cromwell](https://github.com/broadinstitute/cromwell) is aimed at building a cluster environment including the launch of VM just by user inputting user information of each cloud vendor.

In the present situation, it correspond only to Azure, Alpha version.

Visit [GitHub wiki](https://github.com/Rhelixa-inc/RyuGoo-Saba/wiki) for more details.

## Prerequisites
- `docker`
- `docker-compose` (version 3)

## Install
Use `git` to fetch the source from GitHub and use docker-compose to create the CLI environment:

```
$ git clone https://github.com/Rhelixa-inc/RyuGoo-Saba.git
$ docker-compose -f ./RyuGoo-Saba/SabaCLI/docker-compose.CLI.yml up -d --build
$ docker-compose -f ./RyuGoo-Saba/SabaCLI/docker-compose.CLI.yml exec cli bash
$ saba
```

This will do to Create a Docker environment that includes

- SabaCLI
- Ansible
- Azure CLI

The reason to launch the CLI as a Docker-compose environment is to separate the ssh connection information and Azure credential information from those inside the user's PC.

## Construct cluster environment and execute job
```
$ saba start -u [azure-user-id] -p [azure-user-password] -s [azure-subscription-id]
$ saba job submit -s [input-data-urls] -c [cwl-file-urls] -i [instance-size] -d [disk-size]
```

- Launch a VM and do `docker-compose up` as SabaMaster, which will be a job handler.
- Using SabaMaster's REST API endpoint, start another VM and do `docker-compose` up as SabaWorker, which will be a job executer.
- For each job, it is executed in one VM, and when finished job, upload results and log to object storage and delete VM.
