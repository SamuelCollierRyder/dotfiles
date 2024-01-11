return {
  "nvim-neo-tree/neo-tree.nvim",
  branch = "v3.x",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-tree/nvim-web-devicons",
    "MunifTanjim/nui.nvim",
  },
  config = function()
    vim.keymap.set('n', '<leader>f', ':Neotree filesystem reveal bottom<CR>')
    require("neo-tree").setup({
      close_if_last_window = true,
      window = {
        position = "bottom",
        height = 10,
      },
    })
  end
}
