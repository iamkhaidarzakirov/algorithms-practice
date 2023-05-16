# algorithms-practice
Буду публиковать решения некоторых интересных задач, с которыми буду сталкиваться. 

<h2>1. Тренировочный контест Яндекса — contest28412_A.py</h3>
<h3>Андрей и кислота | Задача А.</h3>
<ul>
  <li>Ограничение времени	2 секунды</li>
  <li>Ограничение памяти	512Mb</li>
  <li>Ввод	стандартный ввод или input.txt</li>
  <li>Вывод	стандартный вывод или output.txt</li>
</ul>
<p>Андрей работает в секретной химической лаборатории, в которой производят опасную кислоту с удивительными свойствами. У Андрея есть n бесконечно больших резервуаров, расположенных в один ряд.</p> 
  <p>Изначально в каждом резервуаре находится некоторое количество кислоты. Начальство Андрея требует, чтобы во всех резервуарах содержался одинаковый объем кислоты. К сожалению, разливающий аппарат несовершенен.</p> 
  <p>За одну операцию он способен разлить по одному литру кислоты в каждый из первых k резервуаров. Обратите внимание, что для разных операций k могут быть разными (1 <= k <= n).</p>
  <p>Поскольку кислота очень дорогая,Андрею не разрешается выливать кислоту из резервуаров. Андрей просит вас узнать, можно ли уравнять объемы кислоты в резервуарах.</p> 
  <p>Если это возможно, то посчитать минимальное количество операций, которое потребуется, чтобы этого достичь.</p>
<h4>Формат ввода:</h4>
<ul>
  <li>Первая строка содержит число n (от 1 до 100_000) — количество резервуаров.</li>
  <li>Во второй строке содержатся n целых чисел (от 1 до 10^9) — содержание кислоты в литрах на данный момент</li>
</ul>
<h4>Формат вывода:</h4>
<ul>  
  <li>Если объемы кислоты в резервуарах можно уравнять, выведите минимальное количество операций, необходимых для этого.</li>
  <li>Если это невозможно, выведите «-1».</li>
  </ul>
