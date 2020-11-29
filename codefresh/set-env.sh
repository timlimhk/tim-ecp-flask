#!/bin/bash
git_commit_sha="$(git rev-parse --short HEAD 2>/dev/null)"
if [[ $git_commit_sha == "" ]]
then
     git_commit_sha="undefinedbyCF"
fi

export git_commit_sha
export log_level=INFO
export version=1.0.2
export service_port=5000
export KUBE_CONTEXT=devops-catalog@doc-cf-gke
export CHART_REPO_URL=cm://h.cfcr.io/elitecom/default
export NAMESPACE=default


