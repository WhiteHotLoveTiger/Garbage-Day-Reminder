# Garbage-Day-Reminder
Use AWS Lambda to send yourself SMS reminders about garbage day

### Trigger
My garbage day is Friday, so I have a CloudWatch Event to trigger this function every Thursday evening. Here's my example expression:
`cron(0 22 ? * Thu *)`
Note that the time is in GMT.

### Environment Variables
This function expects a single environment variable called `NUMBERS` to be a comma separated list of phone numbers to send the notifications to. eg. `+15551234567, +15551234567` or just `+15551234567` for a single number.
