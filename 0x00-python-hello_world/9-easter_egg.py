
BISOLA@DESKTOP-K8CPT73 MINGW64 ~
$ ssh 293d6c6dc515@293d6c6dc515.1ed689ad.alx-cod.online
kex_exchange_identification: read: Software caused connection abort
banner exchange: Connection to 3.81.26.228 port 22: Software caused connection abort

BISOLA@DESKTOP-K8CPT73 MINGW64 ~
$ ssh 293d6c6dc515@293d6c6dc515.1ed689ad.alx-cod.online
293d6c6dc515@293d6c6dc515.1ed689ad.alx-cod.online's password:
root@293d6c6dc515:/# ls
alx-low_level_programming      bin   home   libx32  printf  sbin          usr
alx-pre_course                 boot  lib    media   proc    simple_shell  var
alx-system_engineering-devops  dev   lib32  mnt     root    srv
alx-zero_day                   etc   lib64  opt     run     sys
root@293d6c6dc515:/# mkdir alx-higher_level_programming
root@293d6c6dc515:/# ls
alx-higher_level_programming   bin   lib     mnt     run           usr
alx-low_level_programming      boot  lib32   opt     sbin          var
alx-pre_course                 dev   lib64   printf  simple_shell
alx-system_engineering-devops  etc   libx32  proc    srv
alx-zero_day                   home  media   root    sys
root@293d6c6dc515:/# cd alx-higher_level_programming/
root@293d6c6dc515:/alx-higher_level_programming# git init
Initialized empty Git repository in /alx-higher_level_programming/.git/
root@293d6c6dc515:/alx-higher_level_programming# git remote add origin https://github.com/Hameedarh/alx-higher_level_programming.git
root@293d6c6dc515:/alx-higher_level_programming# touch 0x00-python-hello_world
root@293d6c6dc515:/alx-higher_level_programming# ls
0x00-python-hello_world
root@293d6c6dc515:/alx-higher_level_programming# cd 0x00-python-hello_world
bash: cd: 0x00-python-hello_world: Not a directory
root@293d6c6dc515:/alx-higher_level_programming# rm -rf 0x00-python-hello_world
root@293d6c6dc515:/alx-higher_level_programming# ls
root@293d6c6dc515:/alx-higher_level_programming# mkdir 0x00-python-hello_world
root@293d6c6dc515:/alx-higher_level_programming# cd 0x00-python-hello_world/
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 0-run
#!/bin/bash
python3 $PYFILE
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 1-run_inline
#!/bin/bash
python3 <<< $PYCODE
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 10-check_cycle.c
#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        if (!list)
                return (0);

        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (1);
        }

        return (0);
}
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 100-write.py
#!/usr/bin/python3
import sys
sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 101-compile
#!/bin/bash
python3 -m compileall -b $PYFILE i
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 102-magic_calculation.py
#!/usr/bin/python3
def magic_calculation(a, b):
    return (98 + a ** b)
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 2-print.py
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 3-print_number.py
#!/usr/bin/python3
number = 98
print(f"{number:d} Battery street")
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 4-print_float.py
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 5-print_string.py
#!/usr/bin/python3
str = "Holberton School"
print(3 * str)
print(str[:9])
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 6-concat.py
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 += " " + str2
print("Welcome to {}!".format(str1))
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 7-edges.py
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 7-edges.py
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 8-concat_edges.py
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106:112] + str[:6]
print(str)
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 9-easter_egg.py
#!/usr/bin/python3
import this
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>


typedef struct listint_s
{
        int n;
        struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > README.md
0x00-python-hello_world
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git add .
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git commit -m "tasks"
[master (root-commit) ed7a374] tasks
 16 files changed, 90 insertions(+)
 create mode 100644 0x00-python-hello_world/0-run
 create mode 100644 0x00-python-hello_world/1-run_inline
 create mode 100644 0x00-python-hello_world/10-check_cycle.c
 create mode 100644 0x00-python-hello_world/100-write.py
 create mode 100644 0x00-python-hello_world/101-compile
 create mode 100644 0x00-python-hello_world/102-magic_calculation.py
 create mode 100644 0x00-python-hello_world/2-print.py
 create mode 100644 0x00-python-hello_world/3-print_number.py
 create mode 100644 0x00-python-hello_world/4-print_float.py
 create mode 100644 0x00-python-hello_world/5-print_string.py
 create mode 100644 0x00-python-hello_world/6-concat.py
 create mode 100644 0x00-python-hello_world/7-edges.py
 create mode 100644 0x00-python-hello_world/8-concat_edges.py
 create mode 100644 0x00-python-hello_world/9-easter_egg.py
 create mode 100644 0x00-python-hello_world/README.md
 create mode 100644 0x00-python-hello_world/lists.h
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git push --set-upstream origin master
Username for 'https://github.com': Hameedarh
Password for 'https://Hameedarh@github.com':
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 2 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (19/19), 2.29 KiB | 1.14 MiB/s, done.
Total 19 (delta 0), reused 0 (delta 0)
To https://github.com/Hameedarh/alx-higher_level_programming.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > main.p
#!/usr/bin/python3
print("Holberton School")
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git add .
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git commit -m "task"
[master 916b521] task
 1 file changed, 2 insertions(+)
 create mode 100644 0x00-python-hello_world/main.p
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git push --set-upstream origin master
Username for 'https://github.com': Hameedarh
Password for 'https://Hameedarh@github.com':
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 367 bytes | 367.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Hameedarh/alx-higher_level_programming.git
   ed7a374..916b521  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# rm -rf main.p
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > main.py
#!/usr/bin/python3
print("Holberton School")
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git add .
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git commit -m "task"
[master 664a0ce] task
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename 0x00-python-hello_world/{main.p => main.py} (100%)
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git push --set-upstream origin master
Username for 'https://github.com': Hameedarh
Password for 'https://Hameedarh@github.com':
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 300 bytes | 300.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Hameedarh/alx-higher_level_programming.git
   916b521..664a0ce  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# git pull origin master
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 8 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (8/8), 1.64 KiB | 838.00 KiB/s, done.
From https://github.com/Hameedarh/alx-higher_level_programming
 * branch            master     -> FETCH_HEAD
   664a0ce..4c11698  master     -> origin/master
Updating 664a0ce..4c11698
Fast-forward
 0x00-python-hello_world/1-run_inline     |  2 +-
 0x00-python-hello_world/10-check_cycle.c | 25 +++++++++++++++----------
 2 files changed, 16 insertions(+), 11 deletions(-)
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 10-linked_lists.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
        const listint_t *current;
        unsigned int n;

        current = h;
        n = 0;
        while (current != NULL)
        {
                printf("%i\n", current->n);
                current = current->next;
                n++;
        }
        return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
        listint_t *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
        {
                return (NULL);
        }
        new->n = n;
        new->next = *head;
        *head = new;
        return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
        listint_t *current;

        while (head != NULL)
        {
                current = head;
                head = head->next;
                free(current);
        }
}
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 10-main.c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
        listint_t *head;
        listint_t *current;
        listint_t *temp;
        int i;

        head = NULL;
        add_nodeint(&head, 0);
        add_nodeint(&head, 1);
        add_nodeint(&head, 2);
        add_nodeint(&head, 3);
        add_nodeint(&head, 4);
        add_nodeint(&head, 98);
        add_nodeint(&head, 402);
        add_nodeint(&head, 1024);
        print_listint(head);

        if (check_cycle(head) == 0)
                printf("Linked list has no cycle\n");
        else if (check_cycle(head) == 1)
                printf("Linked list has a cycle\n");

        current = head;
        for (i = 0; i < 4; i++)
                current = current->next;
        temp = current->next;
        current->next = head;

        if (check_cycle(head) == 0)
                printf("Linked list has no cycle\n");
        else if (check_cycle(head) == 1)
                printf("Linked list has a cycle\n");

        current = head;
        for (i = 0; i < 4; i++)
                current = current->next;
        current->next = temp;

        free_listint(head);

        return (0);
}

^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 100-write.py
#!/usr/bin/python3
import sys
sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 101-compile
#!/bin/bash
python3 -c "import py_compile; py_compile.compile('$PYFILE', '$PYFILE' + 'c')"
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 102-magic_calculation.py
def magic_calculation(a, b):
    return (98 + a ** b)
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 2-print.py
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 3-print_number.py
#!/usr/bin/python3
number = 98
print("{:d} Battery street".format(number))
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 4-print_float.py
#!/usr/bin/python3
number = 3.14159
print("Float: {:.2f}".format(number))
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 5-print_string.py
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 6-concat.py
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 += (" " + str2)
print("Welcome to {}!".format(str1))
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 7-edges.py
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 8-concat_edges.py
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)
^C
root@293d6c6dc515:/alx-higher_level_programming/0x00-python-hello_world# cat > 9-easter_egg.py
#!/usr/bin/python3
import this
