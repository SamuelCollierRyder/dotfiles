return { 
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000,
    opts = {
        transparent = true,
    },

    config = function()
        require("catppuccin").setup({
            transparent_background = true
        })
        vim.cmd.colorscheme "catppuccin"
    end

}
