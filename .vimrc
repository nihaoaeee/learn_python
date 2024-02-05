

if exists('*minpac#init')
    " Minpac is loaded.
    call minpac#init()
    call minpac#add('k-takata/minpac', {'type': 'opt'})

    "Other plugins
    call minpac#add('tpope/vim-eunuch')
    call minpac#add('yegappan/mru')
endif

if has('eval')
    " Minpac commands
    command! PackUpdate packadd minpac | source $MYVIMRC | call minpac#update('', {'do': 'call minpac#status()'})
    command! PackClean  packadd minpac | source $MYVIMRC | call minpac#clean()
    command! PackStatus packadd minpac | source $MYVIMRC | call minpac#status()
endif

if !has('gui_running')
    " 设置文本菜单
    if has('wildmenu')
        set wildmenu
	set cpoptions-=<
	set wildcharm=<C-Z>
	nnoremap <F10>		:emenu <C-Z>
	inoremap <F10> <C-O> 	:emenu <C-Z>
    endif
endif

if v:version >= 800
    packadd! editexisting
endif

" 切换窗口快捷键映射
nnoremap <C-Tab>	<C-W>w
inoremap <C-Tab>	<C-O><C-W>w
nnoremap <C-S-Tab>	<C-W>W
inoremap <C-S-Tab>	<C-O><C-W>W
