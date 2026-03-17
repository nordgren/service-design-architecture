const fs = require('fs');
const { marked } = require('marked');

const markdown = fs.readFileSync('SYNTHESIS.md', 'utf8');
const html = marked.parse(markdown);

const fullHtml = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Design × Business Architecture × Journey Operations</title>
    <style>
        @media print {
            body { font-size: 11pt; }
            h1 { page-break-before: always; }
            h1:first-of-type { page-break-before: avoid; }
            table { page-break-inside: avoid; }
            pre { page-break-inside: avoid; }
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            color: #1a1a1a;
        }
        h1 { color: #0066cc; border-bottom: 2px solid #0066cc; padding-bottom: 10px; margin-top: 40px; }
        h2 { color: #004499; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin-top: 30px; }
        h3 { color: #333; margin-top: 25px; }
        h4 { color: #555; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; font-size: 14px; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background-color: #f5f5f5; font-weight: 600; }
        tr:nth-child(even) { background-color: #fafafa; }
        code { background-color: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-size: 90%; }
        pre { background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }
        blockquote { border-left: 4px solid #0066cc; margin: 20px 0; padding: 10px 20px; background: #f9f9f9; }
        a { color: #0066cc; }
        hr { border: none; border-top: 1px solid #ddd; margin: 30px 0; }
        .metadata { background: #f0f7ff; padding: 15px; border-radius: 5px; margin-bottom: 30px; }
    </style>
</head>
<body>
${html}
</body>
</html>`;

fs.writeFileSync('SYNTHESIS.html', fullHtml);
console.log('HTML generated: SYNTHESIS.html');
console.log('Size:', (fullHtml.length / 1024).toFixed(1), 'KB');
