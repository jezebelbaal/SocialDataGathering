import datetime

def get_comments_occurrence(db, some_alias):
	print("preparing to load keys to memory")
	full_results = db.keys("comments:" + some_alias + "*")
	print("keys loaded")
	comments_per_date = dict()
	
	for comment_key in full_results:
		comment = db.hmget(comment_key, "created_time")
		comment_date = get_comment_date(comment)

		increment_date(comment_date, comments_per_date)

	return comments_per_date

def get_comment_date(comment_datetime_str):
	comment_datetime = datetime.datetime.strptime(
		comment_datetime_str[0].decode("utf-8"), '%Y-%m-%dT%H:%M:%S+%f')
	return str(comment_datetime.date())

def increment_date(comments_date, comments_per_date):
	if comments_date not in comments_per_date:
		comments_per_date[comments_date] = 0	
	comments_per_date[comments_date] = comments_per_date[comments_date] + 1
	return comments_per_date
