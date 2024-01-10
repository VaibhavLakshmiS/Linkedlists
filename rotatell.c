/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 struct ListNode* tail=head;
 int l=1;
 for (tail;tail->next!=NULL; tail=tail->next){
    l=l+1
 }
 k=k%l
 if ( k==0){
    return head
 }
 struct ListNode* curr = head;
 for (int i=0; i<k-l-1; i++){
    curr=curr->next;
 }
 struct ListNode*newhead=curr;
 curr->next=NULL;
 tail->next=head;
 return newhead;
 