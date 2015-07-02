execute pathogen#infect()
syntax on
colorscheme mustang
filetype plugin indent on
":set nu
:set tabstop=4
:set shiftwidth=4
:set smartindent
:set autoindent
:set hls

:inoremap :ps dprintf(1, "%s\n", );<Esc><left><left>a
:inoremap :pd dprintf(1, "%d\n", );<Esc><left><left>a
:inoremap :pp dprintf(1, "%p\n", );<Esc><left><left>a
:inoremap :pc dprintf(1, "%c\n", );<Esc><left><left>a
:inoremap :pzu dprintf(1, "%zu\n", );<Esc><left><left>a
:inoremap :{ <Esc>:w<Cr>
:inoremap :{} <Esc>:wq<Cr>
:inoremap :armain int		main(int ac, char **av)<cr>{<cr>return (0);<cr>}<up><up><cr>
:inoremap :main int		main(void)<cr>{<cr>return (0);<cr>}<up><up><cr>

let Tlist_Process_File_Always = 1
nmap <silent> <F8> :TagbarToggle<CR>
:set statusline=%<%f%=%([%{Tlist_Get_Tagname_By_Line()}]%)

autocmd bufnewfile *.h so ~/.vim/templates/header_h.txt
autocmd bufnewfile *.h exe "0," . 3 . "g/ndef/s//ndef " .toupper(expand("%:r")).expand("_H")
autocmd bufnewfile *.h exe "0," . 3 . "g/define/s//define " .toupper(expand("%:r")).expand("_H")
autocmd bufnewfile *.h exe "0," . 5 . "g/libft/s//libft"
autocmd bufnewfile *.make so ~/.vim/templates/header_make.txt
