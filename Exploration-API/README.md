# COVID-19-KG-Exploration-API

# 1) Get Publication related to Drugs

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
   "Drugs":[
  	"C0031623",
  	"C0751995",
  	"C0030106"
   ]
}' \
  https://labs.tib.eu/sdm/covid19kg-exp/covid19kg-exp?target=Pub
```

# 2) Get Interactions of a Drug

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
   "Drugs":[
  	"C0000970",
  	"C0028978",
  	"C0009214"
   ]
}' \
  https://labs.tib.eu/sdm/covid19kg-exp/covid19kg-exp?target=DDI&limit=10&page=0
```

# 3) Get all the interaction among the provided Drugs


```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
   "Drugs":[
  	"C0000970",
  	"C0028978",
  	"C0009214"
   ]
}' \
  https://labs.tib.eu/sdm/covid19kg-exp/covid19kg-exp?target=DDIS&limit=10&page=0
```

# 4) Get the predicted interactions of a Drug


```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
   "Drugs":[
  	"C0000970",
  	"C0028978",
  	"C0009214"
   ]
}' \
  https://labs.tib.eu/sdm/covid19kg-exp/covid19kg-exp?target=DDIP&limit=10&page=0
```

# 5) Get all the predicted interaction among the provided Drugs


```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
   "Drugs":[
  	"C0000970",
  	"C0028978",
  	"C0009214"
   ]
}' \
  https://labs.tib.eu/sdm/covid19kg-exp/covid19kg-exp?target=DDIPS&limit=10&page=0
```
