import json
import csv
import codecs



f = codecs.open("verifiedUser-json.json", "r", "utf-8")
data = json.load(f)
f.close()
# codecs.open(file,'w','utf-8')
f = csv.writer(open("data-verified-human-user.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["id", "id_str", "name", "screen_name", "location", "description", "url", "followers_count", "friends_count", "listed_count", "created_at", "favourites_count", "verified", "statuses_count", "lang", "status/text", "has_extended_profile", "default_profile", "default_profile_image"])

for x in data["users"]:
    f.writerow([
        x["id"],
        x["id_str"],
        x["name"].encode("UTF-8"),
        x["screen_name"].encode("UTF-8"),
        x["location"].encode("UTF-8") if x["location"] is not None else x["location"],
        x["description"].encode("UTF-8") if x["description"] is not None else x["description"],
        x["url"].encode("UTF-8") if x["url"] is not None else x["url"],

                x["followers_count"], x["friends_count"], x["listed_count"], x["created_at"], x["favourites_count"],
                x["verified"], x["statuses_count"],
        x["lang"],
        x["status"]["text"].encode("UTF-8") if 'status' in x and x["status"] is not None and x["status"]["text"] is not None else "",
        x["has_extended_profile"],
                x["default_profile"], x["default_profile_image"], "1"])


