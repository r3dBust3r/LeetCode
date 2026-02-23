# Name: unique-email-addresses
# URL: https://leetcode.com/problems/unique-email-addresses/


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniq_emails = set()
        for email in emails:
            addr = ""
            i = 0
            while i < len(email):
                if email[i] == '+':
                    while i < len(email) and email[i] != '@':
                        i += 1
                if email[i] == '@':
                    while i < len(email):
                        addr += email[i]
                        i += 1
                if i < len(email) and email[i].isalnum():
                    addr += email[i]
                i += 1

            uniq_emails.add(addr)

        return len(uniq_emails)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(
    Solution.numUniqueEmails(
        None,
        emails
    )
)
