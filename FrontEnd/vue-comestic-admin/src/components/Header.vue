<template>
    <a-flex
        class="header_section"
        gap="middle"
        justify="flex-end"
        align="center"
    >
        <div class="icon-container">
            <i class="fa-solid fa-bell"></i>
        </div>
        <div class="icon-container">
            <i class="fa-solid fa-message"></i>
        </div>
        <a-dropdown>
            <a class="ant-dropdown-link" @click.prevent>
                <img
                    :src="avatar"
                    alt="Avatar"
                    width="35"
                    height="35"
                    :style="{ borderRadius: '50%' }"
                />
                <DownOutlined />
            </a>
            <template #overlay>
                <a-menu>
                    <a-menu-item>
                        <a class="dropdown-item" href="#">Profile</a>
                    </a-menu-item>
                    <a-menu-item>
                        <a class="dropdown-item" href="#">Settings</a>
                    </a-menu-item>
                    <a-menu-item>
                        <a class="dropdown-item" href="#">Logout</a>
                    </a-menu-item>
                </a-menu>
            </template>
        </a-dropdown>
    </a-flex>
</template>

<script setup lang="ts">
import avatar from "@/assets/logo.jpg";
</script>

<style lang="scss" scoped>
.header_section {
    height: 8vh;
    background-color: #1e293b;
    position: sticky;
    top: 0;
    right: 0;
    padding: 0 20px;
}

.icon-container {
    margin: 0 10px;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
}

.avatar img {
    border: 2px solid white;
}
</style>
