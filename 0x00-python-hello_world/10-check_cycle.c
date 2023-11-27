#include "lists.h"
int check_cycle(listint_t *list)
{
listint_t *one = list;
listint_t *two = list;
while (two && two->next)
{
	one = one->next;
	two = two->next->next;
	if(one == two)
		return (1);
}
return (0);
}
