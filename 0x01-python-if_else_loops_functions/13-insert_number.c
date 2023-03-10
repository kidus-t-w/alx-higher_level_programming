#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc(sizeof(listint_t));
	listint_t *list = *head;
	listint_t *prev;

	if (temp == NULL)
		return (NULL);
	temp->n = number;

	if ((*head) == NULL)
	{
		*head = temp;
		temp->next = NULL;
		return (temp);
	}
	if (list->n > temp->n)
	{
		temp->next = list;
		*head = temp;
		return (temp);
	}
	while(list->next != NULL)
	{
		if (list->n > temp->n)
		{
			temp->next = list;
			prev->next = temp;
			return (temp);
		}
		prev = list;
		list = list->next;
	}
	list->next = temp;
	temp->next = NULL;
	return (temp);
}