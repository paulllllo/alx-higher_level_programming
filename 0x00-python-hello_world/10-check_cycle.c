#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * check_cycle - checks if a cycle exists in a linked list
 * @list: list to be checked
 * Return: 0 is no cycle; 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *head;
	listint_t *temp;
	__attribute__((unused)) int i, compare_i;

	i = 0;
	current = list;
	head = list;
	while (current != NULL)
	{
		compare_i = 0;
		temp = head;
		while (compare_i < i)
		{
			if (current == temp)
				return (1);
			compare_i++;
			temp = temp->next;
		}
		current = current->next;
		i++;
	}
	return (0);
}
