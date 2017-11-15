#Грамматика

* `S -> Word VARLIST;`
* `VARLIST -> AMPERSAND & STAR & WORD, VARLIST`
* `VARLIST -> AMPERSAND & STAR & WORD`
* `VARLIST -> eps`
* `WORD -> [A-Z, a-z] & WORD`
* `WORD -> eps`
* `STAR -> * & STAR`
* `STAR -> eps`
* `AMPERSAND -> &`
* `AMPERSAND -> eps`

Нетерминал    | Значение    
--------------|-------------
S  | Объявление переменных в языке C
WORD | Имя переменной или тип
VARLIST | Список переменных, разделенных запятыми, оканчивающийся на `;`
AMPERSAND | Взятие адреса (&)
STAR | Указатель

##Множества FIRST и FOLLOW для нетерминалов

`c` - любой символ [A-Z, a-z]

Нетерминал | FIRST    | FOLLOW
-----------|----------|-------
S          | `c`      | `$`
WORD       | `c`      | `,`,`;`,` `
STAR       | `*`, eps | `c`
AMPERSAND  | `&`, eps | `*`, `c`
VARLIST    | `c`, `*`, `&`| `;`