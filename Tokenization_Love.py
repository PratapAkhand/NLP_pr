import nltk
nltk.download()

paragraph="""I know we say I love you a lot. In the morning when we wake up, on our way out the door, sometimes when we say goodbye over the phone. We say I love you when something bad happens and we want to let the other person know I’m here for you, we say I love you when one of the kids does something cute or ridiculous. Sometimes, I know, we say I love you when we’re really annoyed with each other. Sometimes we say it after a fight. Other times we say it after making love. We say I love you a lot. I value each and every I love you. They are three little words said so many times and so many different ways and they all add up to a story of our love together and what it means. I wanted to add one more I love you to the bunch—an I love you to let you know that I’m paying attention. When I say I love you and you say I love you too it still means so much to me. It’s such a part of our every days lives, but I’ll never take it for granted. I love you."""
sentences = nltk.sent_tokenize(paragraph)

words= nltk.word_tokenize(paragraph)