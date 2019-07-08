## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:self_intro
- I am [Mary](PERSON)
- My name is [Anna](PERSON)

## intent:give_email
- my email is [john.doe@something.com](email)
- [ion.ion@tiriac.com](email)

## intent:give_tel
- my number is [0123456789](tel)
- contact me at [0987654321](tel)
- you can reach me at [+404567890123](tel)

## regex:tel
- (0)([0-9][\s]*){10}
 
## regex:email
- [\w-]+@([\w-]+\.)+[\w-]+
