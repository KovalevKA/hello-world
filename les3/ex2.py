features = {'Имя': '', 'Фамилия': '', 'Год рождения': '', 'город': '', 'и др.': ''}

def userInput( features):
    for f in features.keys():
        user_data = input('{}: '.format(f))
        features[f] = user_data
    return features

features = userInput(features)

print(features)