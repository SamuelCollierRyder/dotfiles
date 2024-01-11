vim.cmd("set expandtab")
vim.cmd("set tabstop=4")
vim.cmd("set softtabstop=4")
vim.cmd("set shiftwidth=4")
vim.cmd("set relativenumber")
vim.g.mapleader = " "
vim.keymap.set({"n", "v"}, "<leader>p", "\"+p") -- paste from clipboard
vim.keymap.set({"n", "v"}, "<leader>y", "\"+y") -- yank to clipboard
