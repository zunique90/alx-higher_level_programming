#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head node of the list
 *
 * Return: 1 if there is a cycle
 * or 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = (list->next)->next;

	while (fast->next && fast && slow)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = (fast->next)->next;
	}
	return (0);
}
