-- Integrare nvim pentru baza de cunostinte TBF.
-- Pune in init.lua:  require("kb")   (dupa ce adaugi acest folder la runtimepath/packpath)
-- sau, rapid:        :luafile /Users/raztbf/Work/1-tbf-knowledge/lightrag/nvim/kb.lua
--
-- Comenzi:
--   :KB Ce am scris despre nerezonabil?        -> raspuns intr-un scratch buffer
--   :KBmode global                              -> schimba modul (mix/local/global/hybrid/naive)
--   selectezi vizual text, apoi :KB            -> foloseste selectia ca intrebare

local M = {}

local PY = "/Users/raztbf/Work/1-tbf-knowledge/lightrag/.venv/bin/python"
local KB = "/Users/raztbf/Work/1-tbf-knowledge/lightrag/kb.py"
local mode = "mix"

local function show(lines)
  vim.cmd("botright new")
  vim.bo.buftype = "nofile"
  vim.bo.bufhidden = "wipe"
  vim.bo.filetype = "markdown"
  vim.api.nvim_buf_set_lines(0, 0, -1, false, lines)
end

local function ask(question)
  if not question or question == "" then
    vim.notify("KB: nicio intrebare", vim.log.levels.WARN)
    return
  end
  show({ "# KB (" .. mode .. "): " .. question, "", "_se gandeste..._" })
  local out_buf = vim.api.nvim_get_current_buf()
  vim.fn.jobstart({ PY, KB, "-m", mode, question }, {
    stdout_buffered = true,
    on_stdout = function(_, data)
      if data then
        vim.schedule(function()
          if vim.api.nvim_buf_is_valid(out_buf) then
            vim.api.nvim_buf_set_lines(out_buf, 0, -1, false, data)
          end
        end)
      end
    end,
  })
end

vim.api.nvim_create_user_command("KB", function(opts)
  local q = opts.args
  if q == "" and opts.range > 0 then
    -- foloseste selectia/liniile date ca intrebare
    local lines = vim.api.nvim_buf_get_lines(0, opts.line1 - 1, opts.line2, false)
    q = table.concat(lines, " ")
  end
  ask(q)
end, { nargs = "*", range = true })

vim.api.nvim_create_user_command("KBmode", function(opts)
  mode = opts.args
  vim.notify("KB mod: " .. mode)
end, { nargs = 1, complete = function() return { "mix", "local", "global", "hybrid", "naive" } end })

return M
