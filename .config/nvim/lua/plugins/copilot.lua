return {
  "github/copilot.vim",

  config = function()
    vim.keymap.set('i', '<C-1>', '<Plug>(copilot-next)')
    vim.keymap.set('i', '<C-2>', '<Plug>(copilot-previous)')
  end
}
