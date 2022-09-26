
from models import User, Post, db 
from app import app

db.drop_all()
db.create_all()

usr1 = User(first_name="Spongebob", last_name="SquarePants", image_url="https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/SpongeBob_SquarePants_character.svg/1200px-SpongeBob_SquarePants_character.svg.png")
usr2 = User(first_name="Barry", last_name="Bonds", image_url="https://andscape.com/wp-content/uploads/2019/07/Barry-Bonds-Giants-batting.jpg")
usr3 = User(first_name="Dua", last_name="Lipa", image_url="https://media.glamour.com/photos/630506f47cc61d85fe7f1c7a/master/w_2560%2Cc_limit/1161283077")
usr4 = User(first_name="Gordan", last_name="Ramsay", image_url="https://www.grandcentralpublishing.com/wp-content/uploads/2017/06/GR.jpg?resize=500%2C700")
usr5 = User(first_name="Anya", last_name="Taylor-Joy", image_url="https://i.ytimg.com/vi/pMPeaapsVa0/maxresdefault.jpg")

post1 = Post(title="Home Runs", content="I hit home runs", user_id="2")
post2 = Post(title="Chess", content="I am good at Chess", user_id="5")



db.session.add(usr1)
db.session.add(usr2)
db.session.add(usr3)
db.session.add(usr4)
db.session.add(usr5)

db.session.commit()

db.session.add(post1)
db.session.add(post2)

db.session.commit()