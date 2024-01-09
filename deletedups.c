/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* cur = head;
    while ( cur!=NULL){
        while( cur->next && cur->next->val==cur->val){
            cur->next=cur->next->next;
        }
        cur=cur->next;
    }
    return head;
}