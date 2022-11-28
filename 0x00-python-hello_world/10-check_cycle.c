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
	listint_t *i = list;

	if (!list)
		return (0);

	list = list->next;
	while (list)
	{
		if (i == list)
			return (1);
		if (!(list->next) || !(list->next->next))
			return (0);
		i = i->next;
		list = list->next->next;
	}
	return (0);
}
