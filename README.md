# MiniProject3
## Homework: Setup Docker, Flask, SqlAlchmy
Complete this tutorial on getting Docker, Flask, Postgres and SQLalchemy working together:
## Output
We have used the following command :
**INSERT**
```
curl -XPOST -H “Content-type: application/json” -d \
‘{“name”: “catty mcCatFace”, “price”: 5000, “breed”: “bengal”}’ \
‘127.0.0.1:5000/add’
```
![Insert](/images/Insert.png)

**DISPLAY**
```
curl -XGET -H “Content-type: application/json” \
‘127.0.0.1:5000’
```

![Display](/images/Display.png)

