/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        ListNode* temp=head;
        int ans=0;
        int cnt=0;
        while(temp)
        {
            cnt++;
            temp=temp->next;
        }
        temp=head;
        cnt-=1;
        while(temp)
        {
            ans+=pow(2,cnt)*(temp->val);
            cnt--;
            temp=temp->next;
            
        }
        return ans;
        
    }
};
