user = {
    "name": "Test Data",
    "country": "US",
    "city": "NYC",
    "email": "test@test.com",
    "password": "test@1234",
    "address": "NYC near US"
}

sensitive_data = ['password', 'address']

# Delete these sensitive keys

for item in sensitive_data:
    if item in user:
        del user[item]

print(user)