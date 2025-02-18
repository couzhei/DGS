# ⚗️ DGS Project: Automation Initiative

This project aims to streamline and automate the process of account creation through modern Python tooling.

## 🔧 Requirements

- [uv](https://docs.astral.sh/uv/) - The lightning-fast Python package installer and resolver ⚡

## 🎯 Key Features

- 🔄 Fast dependency management
- 📦 Efficient package resolution
- 🔒 Reliable dependency locking
- ⚡ Lightning-fast virtual environments
- 🎨 Modern linting and formatting tools

## 🚀 Setup

1. **Install uv** 🛠️

   If you don't have `uv`, yet run this command:
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   

2. **Project Setup** 🏗️

   Simply run:
   ```sh
   uv run -m fastapi run
   ```
   And installation of packages will be taken care of as well as your running app.

3. **Development Server** 💻

   Launch the FastAPI development server:
   ```sh
   uv run -m fastapi run
   ```

## 📝 Managing Dependencies

### Adding New Packages 📦

```sh
uv add <package-name>
```

### Syncing Environment 🔄

```sh
uv sync
```

<!-- ## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request -->

## 📚 Additional Resources

- [uv Documentation](https://docs.astral.sh/uv/) 📖
- [FastAPI Documentation](https://fastapi.tiangolo.com/) 🚀
- [Python Package Index](https://pypi.org) 🐍
- [ruff](https://docs.astral.sh/ruff/tutorial/)⚖️
