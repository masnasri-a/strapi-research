import mysql.connector


insert = "INSERT INTO `admin_users` (`id`, `firstname`, `lastname`, `username`, `email`, `password`, `reset_password_token`, `registration_token`, `is_active`, `blocked`, `prefered_language`, `created_at`, `updated_at`, `created_by_id`, `updated_by_id`) VALUES (NULL, 'nasri', 'author', 'nasri.author', 'nasri.author@gmail.com', '$2a$10$NwM.ShKP3EbDSdCaRAqQo.jz5ZC30unKU7BvxyGHXC6RuypFC3gGm', NULL, NULL, '1', NULL, NULL, '2022-11-16 23:51:40.000000', '2022-11-16 23:51:40.000000', '1', '1');"
def connect():
    mydb = mysql.connector.connect(
    host="103.176.79.228",
    user="root",
    password="UtyCantik12",
  database="strapi"
    )

    return mydb

def select(username):
    mydb = connect()
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM admin_users WHERE username = '{str(username).replace(' ','-')}'")
    myresult = mycursor.fetchone()
    return myresult

def create_user(username, role):
    query = f"INSERT INTO `admin_users` (`id`, `firstname`, `lastname`, `username`, `email`, `password`, `reset_password_token`, `registration_token`, `is_active`, `blocked`, `prefered_language`, `created_at`, `updated_at`, `created_by_id`, `updated_by_id`) VALUES (NULL, '{username}', 'author', '{str(username).replace(' ','-')}', '{str(username).replace(' ','-')}@gmail.com', '$2a$10$NwM.ShKP3EbDSdCaRAqQo.jz5ZC30unKU7BvxyGHXC6RuypFC3gGm', NULL, NULL, '1', NULL, NULL, '2022-11-16 23:51:40.000000', '2022-11-16 23:51:40.000000', '1', '1');"
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    ids = mycursor.lastrowid

    role_id = 3

    if role == 'author':
        role_id = 3
    elif role == 'editor':
        role_id = 2
    elif role == 'super admin':
        role_id = 1

    query_role = f"INSERT INTO `admin_users_roles_links` (`id`, `user_id`, `role_id`, `role_order`, `user_order`) VALUES (NULL, '{ids}', '{role_id}', '1', '1');"
    mycursor.execute(query_role)
    mydb.commit()

    ids = mycursor.lastrowid
    print('insert id = ',ids)

def upsert(username):
    get_data = select(username)
    if get_data is None:
        create_user(username,'author')
        print(f'create user {username} successfully')
    else:
        print('user already')

def set_author(username):
    name = select(username)
    if name != None:
        mydb = connect()
        mycursor = mydb.cursor()
        ids = name[0]
        print(ids)
        query = f"UPDATE `wordpresses` SET `created_by_id` = '{ids}', `updated_by_id` = '1' WHERE `wordpresses`.`dc_creator` = '{username}';"
        mycursor.execute(query)
        mydb.commit()
        print(f'update {username} success')
if __name__ == "__main__":
    # select('masnasri')
    # create_user('masnasri', 'author')
    # upsert('nanas')
    set_author('nasriblog12')