#include "lists.h"
/**
 * insert_node - inserts a new node at a given position
 * @head: pointer to the head node of the list
 * @number: number to be added
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);

	newnode->n = number;

	if (*head)
	{
		temp = *head;
		if (number <= temp->n)
		{
			newnode->next = temp;
			*head = newnode;
		}
		else
		{
			while (number > (temp->next)->n)
			{
				temp = temp->next;
				if (!temp->next)
					break;
			}
			newnode->next = temp->next;
			temp->next = newnode;
		}
	}
	else
	{
		newnode->next = NULL;
		*head = newnode;
	}
	return (newnode);
}
