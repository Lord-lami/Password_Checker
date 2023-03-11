import requests
import hashlib
import sys

sha1hash =  '5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8'

def get_pwned_query(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	return sha1password[0:5], sha1password[5:]

def request_api_data(query):
	api_url = 'https://api.pwnedpasswords.com/range/' + str(query)
	response = requests.get(api_url)
	if rsc := response.status_code == 200:
		return response
	else:
		raise RuntimeError(f'Error fetching: {rsc}')


def search_response(response, hash_remaining):
	hash_n_count = dict()
	# print(response.text)
	for line in response.text.splitlines():
		hashes, count = line.split(':')
		if hashes ==  hash_remaining:
			return count

	return 0



def find_password_leaks(password):
	query, remaining = get_pwned_query(password)
	search_results = request_api_data(query)
	return search_response(search_results, remaining)

def main(args):
	details = dict()
	for password in args:
		details.update({password: int(find_password_leaks(password))})

	print(details)

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
