#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to pointer of the head of the list
 * Return: pointer to the head of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev, *next;

	if (head == NULL || *head == NULL)
		return (NULL);

	prev = NULL;
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		if (!next)
			break;
		*head = next;
	}

	return (*head);
}

/**
 * cmp_lists - is two lists equals
 * @head1: head first list
 * @head2: head second list
 * Return: 1 if true else false
 */

int cmp_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}
	return (head1 == NULL && head2 == NULL);
}

/**
 * is_palindrome - is list plandrome
 * @head: pointer to head
 * Return: 1 if true else false
 */

int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *second = *head;
	listint_t *temp = *head;
	listint_t *headSecond = NULL;
	int isPalindrome;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (second != NULL && second->next != NULL)
	{
		second = second->next->next;
		temp = first;
		first = first->next;
	}
	if (second != NULL)
	{
		first = first->next;
	}
	temp->next = NULL;
	headSecond = first;
	reverse_listint(&headSecond);
	isPalindrome = cmp_lists(*head, headSecond);
	reverse_listint(&headSecond);
	return (isPalindrome);
}

