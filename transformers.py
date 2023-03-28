"""This module contains functions for transforming between coordinate systems."""
#pylint: disable=invalid-name
import numpy as np

def camera(focal_length=1) -> np.ndarray:
    """Return the camera matrix.
    
    Args:
        focal_length (float): The focal length of the camera.

    Returns:
        np.ndarray: The camera matrix.
    """
    return np.array([
        [focal_length, 0, 0, 0],
        [0, focal_length, 0, 0],
        [0, 0, 1, 0]
    ])

def translate(x=0, y=0, z=0) -> np.ndarray:
    """Return the translation matrix.

    Args:
        x (float): The translation in the x direction.
        y (float): The translation in the y direction.
        z (float): The translation in the z direction.

    Returns:
        np.ndarray: The translation matrix.
    """
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

def scale(x=1, y=1, z=1) -> np.ndarray:
    """Return the scale matrix.

    Args:
        x (float): The scale in the x direction.
        y (float): The scale in the y direction.
        z (float): The scale in the z direction.

    Returns:
        np.ndarray: The scale matrix.
    """
    return np.array([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ])

def rotate_x(theta) -> np.ndarray:
    """Return the rotation matrix about the x axis.

    Args:
        theta (float): The rotation angle.

    Returns:
        np.ndarray: The rotation matrix.
    """
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

def rotate_y(theta) -> np.ndarray:
    """Return the rotation matrix about the y axis.

    Args:
        theta (float): The rotation angle.

    Returns:
        np.ndarray: The rotation matrix.
    """
    return np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

def rotate_z(theta) -> np.ndarray:
    """Return the rotation matrix about the z axis.

    Args:
        theta (float): The rotation angle.

    Returns:
        np.ndarray: The rotation matrix.
    """
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def world_to_screen(camera_pitch, camera_yaw, \
                    camera_origin, focal_length) -> np.ndarray:
    """Return the world to screen matrix.

    Args:
        camera_pitch (float): The pitch of the camera.
        camera_yaw (float): The yaw of the camera.
        camera_origin (np.ndarray): The origin of the camera.
        focal_length (float): The focal length of the camera.

    Returns:
        np.ndarray: The world to screen matrix.
    """
    return camera(focal_length) @ rotate_x(camera_pitch) @ \
        rotate_y(camera_yaw) @ translate(*(-camera_origin.flat[:-1]))
