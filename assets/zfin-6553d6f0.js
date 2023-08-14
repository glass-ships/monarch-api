const A="data:image/png;base64,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";export{A as default};