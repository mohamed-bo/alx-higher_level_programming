#include <Python.h>
#include <object.h>

/**
 * print_python_list_info - print list info
 * @p: Pyobjext adress
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size = PyList_Size(p);
	PyListObject *objec;

	objec = (PyListObject *)p;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", objec->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(objec->ob_item[i])->tp_name);
	}
}
