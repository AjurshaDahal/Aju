from ovs.registration import register_voter

# Example test data
voter_data = {
    'name': 'John Doe',
    'id': 'VOTER123',
    'dob': '1990-01-01',
    'address': '123 Main St'
}

# Call the function
register_voter(voter_data)

