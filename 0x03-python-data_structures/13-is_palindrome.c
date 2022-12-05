#include "lists.h"
/**
 * reverse_listint - reverses a listint_t list
 * @head: pointer to the head node of the list
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *copy, *temp;

	if (head == NULL || *head == NULL)
		return (NULL);

	copy = NULL;
	while ((*head)->next != NULL)
	{
		temp = (*head)->next;
		(*head)->next = copy;
		copy = *head;
		*head = temp;
	}
	(*head)->next = copy;

	return (*head);
}
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to the head node of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reversed, *center;
	size_t len = 0;
	size_t i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		len++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		temp = temp->next;
	if ((len % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reversed = reverse_listint(&temp);
	center = reversed;

	temp = *head;
	while (reversed)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	reverse_listint(&center);

	return (1);
}
