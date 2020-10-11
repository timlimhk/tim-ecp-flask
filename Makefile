## Composes test environment using docker-compose
GIT_SHA=$(shell git rev-parse --short HEAD)
CI_USER=timlimhk
DK_PASSWORD=##PASSWORD###
HELM_REPO=https://timlimhk.github.io/helm-chart/ 

dk_build:
	@echo Building container
	sed -i "s/git_commit_sha=.*/git_commit_sha=$(GIT_SHA)/" ./docker-compose.yml
	docker-compose -f ./docker-compose.yml build

# WIP for login with password
dk_push:
	#docker login --username $(CI_USER) --password $(DK_PASSWORD)
	docker tag $(CI_USER)/tim-ecp-flask:latest $(CI_USER)/tim-ecp-flask:$(GIT_SHA) 
	docker push $(CI_USER)/tim-ecp-flask:$(GIT_SHA) 

dk_stop:
	@echo Stopping container
	docker-compose -f ./docker-compose.yml down -v
dk_start:
	@echo Starting container
	docker-compose -f ./docker-compose.yml up -d --force-recreate

h_pack:
	@echo Packaging Helm Chart
	sed -i "s/git_commit_sha=.*/git_commit_sha=$(GIT_SHA)/" ./chart/values.yaml
	helm package chart -d chart
	helm repo index --url $(HELM_REPO) chart

h_pack_remote:
	@echo Packaging Helm Chart Push to remote 
	sed -i "s/git_commit_sha=.*/git_commit_sha=$(GIT_SHA)/" ./helm-chart/charts/tim-ecp-flask/values.yaml
	helm package ./helm-chart/charts/tim-ecp-flask -d ./helm-chart
	helm repo index --url $(HELM_REPO) ./helm-chart
	(cd ./helm-chart; git add . && git commit -m "commit" && git push origin master)

# WIP
h_push:
	@echo Pushing Helm Chart
	#  Need to work out how to git in git
	#git commit -a -m "change index"
	#git push origin

h_repo:
	@echo Add Helm Repo
	helm repo add myhelmrepo $(HELM_REPO) 
	helm repo list

h_inst:
	@echo Installing Helm chart 
	sed -i "s/git_commit_sha=.*/git_commit_sha=$(GIT_SHA)/" ./chart/values.yaml
	helm install tim-ecp-flask chart

h_uninst:
	@echo Uninstalling Helm chart 
	helm uninstall tim-ecp-flask
