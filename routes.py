from flask import render_template, request,jsonify,redirect,url_for
from models import User

def register_routes(app,db):
    @app.route('/', methods =['GET','POST'])
    
    def index():
        if request.method == 'GET':
            
            users = User.query.all() 
            return render_template(template_name_or_list='index.html', users=users)
             
                  

        elif request. method== 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            contact = request.form.get('contact')
            
            user = User(name= name, email= email)
            
            db.session.add(user)
            db.session.commit()

            users = User.query.all()
            return render_template(template_name_or_list='index.html', users= users)     
               
    
    
    
    
    @app.route('/get_users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify ([{"name": user.name, "email":user.email}for user in users])
    
    @app.route('/add_user', methods=['POST'])
    def add_user():
        data = request.get_json()
        if not data or "name" not in data or "email" not in data:
            return jsonify({"error:" : "name is required"}),400
        user = User(name= data['name'], email= data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User updated"})
    
    @app.route('/delete_user/<uid>', methods=['DELETE'])
    def delete_user(uid):
        User.query.filter(User.uid == uid).delete()
        db.session.commit()
        return jsonify ({"message": "User deleted"})
    
    
    @app.route('/update_user/<int:uid>', methods=['PUT'])
    def update_user(uid):
        user = User.query.get(uid)

        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()

        if not data or ("name" not in data and "email" not in data):
            return jsonify({"error": "At least one field (name or email) is required"}), 400

    # Update only the provided fields
        if "name" in data:
            user.name = data["name"]
        if "email" in data:
            user.email = data["email"]

        db.session.commit()

        return jsonify({"id": user.uid, "name": user.name,"email": user.email}), 200 # Convert user to dict before returning

    
    

               
    
    @app.route('/delete/<uid>', methods=['DELETE'])
    def delete(uid):
        User.query.filter(User.uid == uid).delete()
        
        db.session.commit()
        
        users = User.query.all()
        
        return render_template(template_name_or_list='index.html', users = users)         
    
    @app.route('/update/<uid>', methods=['GET', 'POST'])
    def update(uid):
            user = User.query.get(uid) 
                   
            if not user:
                return jsonify({"error": "user not found" })
            if request.method=='POST':
                user.name = request.form.get("name", user.name)  # Keep old value if field is empty
                user.email = request.form.get("email", user.email)
                user.contact = request.form.get("contact", user.contact)
           
                db.session.commit()
                return redirect(url_for('index'))

            
            return render_template('update.html', user=user)
        
    @app.route('/details/<uid>', methods=['GET'])
    def details(uid):
        user = User.query.filter(User.uid == uid).first()
        return render_template(template_name_or_list='details.html', user=user)
         
    
      
        