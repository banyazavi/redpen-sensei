import requests

def get_daily_challenge():
    leetcode_host = 'https://leetcode.com'
    leetcode_graphql = leetcode_host + '/graphql'
    query = '''
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            link
            question {
                frontendQuestionId: questionFrontendId
                title
                difficulty
            }
        }
    }
    '''

    challenge_data = requests.post(leetcode_graphql, json={'query': query}).json()['data']['activeDailyCodingChallengeQuestion']

    return {
        'date': challenge_data['date'],
        'link': leetcode_host + challenge_data['link'],
        'id': challenge_data['question']['frontendQuestionId'],
        'title': challenge_data['question']['title'],
        'difficulty': challenge_data['question']['difficulty']
    }
