#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts number in sorted list
 * @head: adress of head
 * @number: number
 * Return: the address of the newnode node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode;
    listint_t *temp;

    if (!head)
        return (NULL);
    newnode = malloc(sizeof(listint_t));
    if (!newnode)
        return (NULL);
    newnode->n = number;
    if (!*head)
    {
        newnode->next = NULL;
        *head = newnode;
        return (newnode);
    }
    temp = *head;
    if (temp->n > number)
    {
        newnode->next = temp;
        *head = newnode;
        return (newnode);
    }
    while (temp->next)
    {
        if (temp->next->n > number)
        {
            newnode->next = temp->next;
            temp->next = newnode;
            return (newnode);
        }
        temp = temp->next;
    }
    newnode->next = NULL;
    temp->next = newnode;
    return (newnode);
}

