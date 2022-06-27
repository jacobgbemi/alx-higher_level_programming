#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * @list: linked list
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *next_node = list;
	listint_t *prev_node = list;

	if (!list)
		return (0);

	while (1)
	{
		if (next_node->next != NULL && next_node->next->next != NULL)
		{
			next_node = next_node->next->next;
			prev_node = prev_node->next;

			if (next_node == prev_node) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
