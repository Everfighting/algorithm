//选择排序
public static void SelectionSort(int[] list)
  {
    int temp;
    for (int i= 0;i<list.length;i++)
    {
      for (int j = i + 1;j<list.length;j++)
      {
        if (list[j] < list[min])
        {
          min = j;
        }
      }
      temp = list[i];
      list[i] = list[min];
      list[min] = temp;
    }
  }
